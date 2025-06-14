library(ggplot2)
library(ggpubr)
library(tidyverse)
library(broom)
library(rockchalk)
library(multcomp)
library(rstatix)

setwd('C:/Users/lenovo/Desktop/PhD/course regis/Comp Psycholing/data_for_R')

data.cosine <- read.csv(file = 'data_cosine_w7s150.csv')

# combine condition unrel_strong & unrel_weak into one condition: unrel
data.cosine$condition = as.factor(data.cosine$condition)
levels(data.cosine$condition)[levels(data.cosine$condition)%in%c("unrel_strong","unrel_weak")] <- "unrel"
# choose only data wit 50-ms isi
data.cosine.combined.50isi <- data.cosine[which(data.cosine$isi==50),]

# one-way ANOVA: strong vs weak vs unrel
one.way <- aov(cosine ~ condition, data = data.cosine.combined.50isi)
summary(one.way)

# multiple pairwise comparisons
tukey <- glht(one.way, linfct = mcp(condition = "Tukey"))
summary(tukey)


# Plotting
stat.test <- data.cosine.combined.50isi %>% t_test(cosine ~ condition)
stat.test <- stat.test %>%
  add_y_position()
# set colors, patterns, etc.
bp <- ggboxplot(data.cosine.combined.50isi, x = "condition", y = "cosine", 
            color = "condition", palette = "Greys", shape = "condition",
            order = c("strong", "weak", "unrel"),
            ylab = "Cosine value", xlab = "Condition") +
  geom_point(position = "jitter", alpha = 1/100,
            colour = "black", fill = "white")
# add significance labels
if(require("ggpubr")){
  bp + stat_pvalue_manual(stat.test, label = "p.adj.signif", tip.length = 0.001)}


barp <- ggbarplot(data.cosine.combined.50isi, x = "condition", y = "cosine", add = "mean_se",
          fill = "condition",
          order = c("strong", "weak", "unrel"),
          ylab = "Cosine value", xlab = "Condition") +
  scale_fill_brewer(palette = "Greys", direction = -1)
if(require("ggpubr")){
  barp + stat_pvalue_manual(stat.test, label = "p.adj.signif", tip.length = 0.001)}
