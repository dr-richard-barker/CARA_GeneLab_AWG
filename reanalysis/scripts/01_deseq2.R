#!/usr/bin/env Rscript
# OSD-120 differential expression (DESeq2) — flight vs ground within each Ecotype x Treatment.
# Input : raw gene x sample count matrix + sample metadata (Ecotype, Treatment, Spaceflight)
#         Get processed data from OSDR:  https://osdr.nasa.gov/osdr/data/osd/files/120
# Output: per-contrast DE tables + one tidy combined table under results/de/.
suppressMessages({library(DESeq2); library(dplyr); library(tidyr); library(readr); library(tibble)})

counts_file <- Sys.getenv("OSD120_COUNTS", "data/OSD-120_rnaseq_raw_counts.csv")  # TODO: OSDR RSEM/STAR counts
meta_file   <- Sys.getenv("OSD120_META",   "data/OSD-120_samples.csv")            # cols: sample,Ecotype,Treatment,Spaceflight
outdir <- "results/de"; dir.create(outdir, recursive = TRUE, showWarnings = FALSE)

cts  <- as.matrix(read.csv(counts_file, row.names = 1, check.names = FALSE))
meta <- read.csv(meta_file, row.names = 1, check.names = FALSE)
meta <- meta[colnames(cts), , drop = FALSE]
stopifnot(all(c("Ecotype","Treatment","Spaceflight") %in% colnames(meta)))

short <- function(x) gsub("[^A-Za-z0-9]", "", x)
meta$eco <- short(meta$Ecotype); meta$trt <- short(meta$Treatment); meta$fly <- short(meta$Spaceflight)
meta$group <- factor(paste(meta$eco, meta$trt, meta$fly, sep = "_"))

dds <- DESeqDataSetFromMatrix(round(cts), meta, design = ~ group)
dds <- dds[rowSums(counts(dds)) >= 10, ]
dds <- DESeq(dds)

flyL   <- unique(meta$fly)
flight <- grep("Space|Flight", flyL, value = TRUE)[1]
ground <- grep("Ground",       flyL, value = TRUE)[1]
combos <- unique(meta[, c("eco","trt")])

all_res <- list()
for (i in seq_len(nrow(combos))) {
  e <- combos$eco[i]; t <- combos$trt[i]
  g1 <- paste(e, t, flight, sep = "_"); g0 <- paste(e, t, ground, sep = "_")
  if (!all(c(g1, g0) %in% levels(meta$group))) next
  df <- results(dds, contrast = c("group", g1, g0)) |> as.data.frame() |>
        rownames_to_column("gene") |>
        mutate(ecotype = e, treatment = t, contrast = paste0(g1, " vs ", g0))
  all_res[[paste(e, t, sep = "_")]] <- df
  write_csv(df, file.path(outdir, sprintf("DE_%s_%s_flight_vs_ground.csv", e, t)))
}
write_csv(bind_rows(all_res), file.path(outdir, "DE_all_flight_vs_ground_tidy.csv"))
message("wrote ", length(all_res), " flight-vs-ground contrasts to ", outdir)
