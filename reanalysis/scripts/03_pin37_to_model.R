#!/usr/bin/env Rscript
# Bridge: turn the measured PIN3/PIN7 (columella) flight fold-change into the Virtual Root
# `pin37` parameter and emit a shareable URL that reproduces the microgravity auxin map.
#   pin37 = 1  -> 1 g (full columella PIN3/7);  pin37 < 1 -> spaceflight suppression.
suppressMessages({library(dplyr); library(readr)})

aux <- read_csv("results/auxin_machinery_FC.csv", show_col_types = FALSE)

# Choose the condition to model (default: WT Col-0, Light). Edit to taste.
ecotype_sel   <- Sys.getenv("VR_ECOTYPE",   "Col0")
treatment_sel <- Sys.getenv("VR_TREATMENT", "LightTreatment")

sel <- aux |> filter(symbol %in% c("PIN3","PIN7"),
                     grepl(ecotype_sel, ecotype, ignore.case = TRUE),
                     grepl(treatment_sel, treatment, ignore.case = TRUE))
if (nrow(sel) == 0) sel <- filter(aux, symbol %in% c("PIN3","PIN7"))   # fall back to all rows

fc    <- mean(2 ^ sel$log2FoldChange, na.rm = TRUE)   # linear flight/ground
pin37 <- max(0, min(1, round(fc, 2)))                 # model expects 0..1
cat(sprintf("mean PIN3/7 flight fold-change = %.2f  ->  pin37 = %.2f\n", fc, pin37))

base <- "https://dr-richard-barker.github.io/virtual-root/"
url  <- sprintf("%s#p=16&a=42&q=0.025&k=0.0012&c=%.2f&g=0&m2=0&m1=0&d=0", base, pin37)
cat("\nVirtual Root microgravity scenario (share / embed for Figure 3):\n", url, "\n")
dir.create("results", showWarnings = FALSE)
writeLines(url, "results/virtual_root_uG_url.txt")
