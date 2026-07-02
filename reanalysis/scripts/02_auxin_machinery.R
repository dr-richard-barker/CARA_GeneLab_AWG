#!/usr/bin/env Rscript
# Extract the auxin transport/response machinery from the flight-vs-ground DE tables,
# so PIN3/PIN7 (the columella carriers) can drive the microgravity auxin model.
suppressMessages({library(dplyr); library(readr); library(ggplot2)})

tidy <- read_csv("results/de/DE_all_flight_vs_ground_tidy.csv", show_col_types = FALSE)

genes <- tibble::tribble(
  ~symbol, ~AGI,
  "PIN1","AT1G73590", "PIN2","AT5G57090", "PIN3","AT1G70940", "PIN4","AT2G01420", "PIN7","AT1G23080",
  "AUX1","AT2G38120", "LAX1","AT5G01240", "LAX2","AT2G21050", "LAX3","AT1G77690",
  "TIR1","AT3G62980", "AFB2","AT3G26810", "ARR5","AT3G48100",
  "ARF7","AT5G20730", "ARF19","AT1G19220", "IAA14","AT4G14550"
)

aux <- tidy |> mutate(AGI = toupper(gene)) |> inner_join(genes, by = "AGI") |>
       select(symbol, AGI, ecotype, treatment, log2FoldChange, padj)
write_csv(aux, "results/auxin_machinery_FC.csv")

ggplot(aux, aes(paste(ecotype, treatment), log2FoldChange, fill = log2FoldChange < 0)) +
  geom_col() + facet_wrap(~symbol) + coord_flip() +
  labs(title = "OSD-120 flight vs ground: auxin machinery",
       x = NULL, y = "log2 fold-change (flight / ground)") +
  theme_minimal(base_size = 10) + theme(legend.position = "none")
ggsave("results/auxin_machinery_FC.png", width = 9, height = 7, dpi = 130)

message("PIN3 / PIN7 (the model-relevant carriers):")
print(dplyr::filter(aux, symbol %in% c("PIN3","PIN7")))
