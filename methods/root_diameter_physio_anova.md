# root\_diameter\_physio\_anova

```{r
knitr::opts_chunk$set(echo=TRUE, comment=NA, tidy=TRUE, tidy.opts=list(width.cutoff=60), warning=FALSE, message=FALSE)
library(knitr)
library(ggplot2)
library(dplyr)
library(R.matlab)
library(tidyverse)
library(ggpubr)
library(rstatix)
```

### Get physiology data that is only day 11 year old

```{r}
df <- read.csv("root_11_clean.csv")
```

```{r}
df
```

```{r}
group_by(df, Control) %>%
  summarise(
    count = n(),
    mean = mean(diameter, na.rm = TRUE),
    sd = sd(diameter, na.rm = TRUE)
  )
```

### One-way ANOVA

> Is there signficant difference in average diameter between different control group (All 12 = 3 genotypes/2 Gravity/2 Light) ?

```{r}
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Control), data = df)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

```{r}
x<-TukeyHSD(res.aov)$`factor(Control)`
#x
```

> Is there signficant difference in average diameter between different genotype (3 genotypes) ?

```{r}
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Ecotype.Genotype), data = df)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

> Is there signficant difference in average diameter between different gravity treatment (2 gravity) ?

```{r}
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Spaceflight.Treatment), data = df)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

> Is there signficant difference in average diameter between different light treatment(2 light) ?

```{r}
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Illumination.trestment.2), data = df)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

> Is there significant difference in average diameter between different gravity treatment (2 gravity) within same genotype?

* Col

```{r}
col <- read.csv("root_11_clean_col.csv")
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Spaceflight.Treatment), data = col)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

* PhyD

```{r}
phyd <- read.csv("root_11_clean_phyd.csv")
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Spaceflight.Treatment), data = phyd)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

* WS

```{r}
ws <- read.csv("root_11_clean_ws.csv")
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Spaceflight.Treatment), data = ws)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

> Is there signficant difference in average diameter between different light treatment (2 light) within same genotype?

* Col

```{r}
#col <- read.csv("root_11_clean_col.csv")
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Illumination.trestment.2), data = col)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

* PhyD

```{r}
#col <- read.csv("root_11_clean_col.csv")
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Illumination.trestment.2), data = phyd)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

* WS

```{r}
#col <- read.csv("root_11_clean_col.csv")
# Compute the analysis of variance
res.aov <- aov(diameter ~ factor(Illumination.trestment.2), data = ws)
# Summary of the analysis
summary(res.aov)
```

```{r}
TukeyHSD(res.aov)
```

```{r}
```
