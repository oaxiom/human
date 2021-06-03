
# EDASeq-based GC normlisation of data
library('data.table')
library("EDASeq")

#setwd('/Volumes/RAID1/big_mouse/mouse/te_counts') # For RStudio;

count_table <- data.frame(fread("norm_input.tsv"), row.names='ensg')

# Filtering criteria:
filter_threshold = 10^1.6 # number of tags in <num_conditions> conditions to consider expressed (This number is POST normalisation)
num_conditions = 2 # number of conditions that must be greater than <filter_threshold>
# Because of the lack of robust replicates and the relatively high filter_threshold
# It is better to keep this value low. As it might bias genes who are only expressed in a single cell type
# Against being detected.

# Load data:
gc = data.frame(fread("../hg38/hg38_gencode_ensg_tes_gc_percent_v32.txt"), row.names=1) # The /100.0 is not required
design = data.frame(1:dim(count_table)[2], row.names=colnames(count_table))
rownames(design) = colnames(count_table)

# Make sure gc and count_table match exactly
common = intersect(rownames(gc), rownames(count_table))
df = data.frame(gc=gc, spaz=gc)
feature = df[common,]
colnames(feature) = c("gc", "fill")
count_table = count_table[common,]

pdf("LibSizes.pdf")
sums = colSums(count_table)
m = mean(colSums(count_table))
s = sd(colSums(count_table))
hist(colSums(count_table), breaks=200, main="Mapped Library Sizes", xlab="Number of mapped sequence tags")
abline(v=m, col="red")

#abline(v=m+s, col="blue")
#abline(v=m-s, col="blue")
#sums[sums==min(sums)]
#sums[sums==max(sums)]
dev.off()

pdf("GeneSizes.pdf")
sums = rowSums(count_table)
m = mean(log10(sums))
s = sd(log10(sums))
hist(log10(sums), breaks=50, main="Mapped Library Sizes", xlab="Number of mapped sequence tags")
abline(v=m, col="red")
abline(v=m+s, col="blue")
abline(v=m-s, col="blue")
sums[sums==max(sums)]
dev.off()

# QC histograms
pdf("QC_histograms.pdf", width=7, height=7)
for (i in 2:dim(count_table)[2]){
  title = colnames(count_table)[i]
  plot(density(log10(count_table[,i])), main=title, xlim=c(-1, 6), ylim=c(0, 0.55))
}
dev.off()

pdf("biasplots.pdf", width=15, height=7)
par(mfrow=c(1,2))
plot(density(log10(count_table[,1])), main="Before Norm", ylim=c(0, 0.55))
for (i in 2:dim(count_table)[2]){
  lines(density(log10(count_table[,i])))
}

data <- newSeqExpressionSet(counts=as.matrix(count_table), featureData=feature, 
                            phenoData=design) # will only tolerate integers

#biasPlot(data, "gc", log=T, ylim=c(-4,8))

# normalise
cdswithin = withinLaneNormalization(data, "gc", which="full")
cdsnormed = betweenLaneNormalization(cdswithin, which="full")

norm_table = normCounts(cdsnormed)
plot(density(log10(count_table[,1])), main="Post Norm", ylim=c(0, 0.45))
#for (i in 2:dim(norm_table)[2]){ # only enable if which != "full"
#  lines(density(log10(norm_table[,i])))
#}
abline(v=log10(filter_threshold), col="grey")
#biasPlot(cdsnormed, "gc", log=T, ylim=c(-4,8))

# Filter lowly expressed
keep <- rowSums(norm_table>filter_threshold) >= num_conditions # Filtering must be done here BEFORE DE.
norm_table = norm_table[keep,]
print(paste("Kept:", dim(norm_table)[1]))

dev.off()

write.table(norm_table, "rawtags_gc_normed.tsv", sep="\t", col.names=NA)

