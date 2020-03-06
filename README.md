*Full paper available at /Reports/Moon_BE498_paper.docx*
*Refer to paper for information on independent/dependent variables*

# Abstract
Marijuana is one of the most widely used illicit substance worldwide.  Its potential medicinal use has garnered much attention in the scientific community, and studies of both its negative and positive aspects have been steadily increasing in the past few years.  Using a sample population of veterans in Santa Cruz, California, this study observes the effects of cannabis use with regard to three measures of mental health that address dependency, depression, anxiety and post-traumatic stress disorder.  Using Welch’s t-test, Mann-Whitney U test, and randomization, the null hypothesis, which states that there is no difference in mean between two groups categorized by frequency and amount of cannabis use, was tested.  The results showed statistical significance only with the measure that evaluates depression and anxiety, favoring the alternative hypothesis that asserted an improved mental state with greater use.  These results however, must be interpreted with caution, as a multitude of limitation, both within the data and the testing methods, exist.  A more carefully controlled study, as well as more powerful testing methods, would be required to obtain even more accurate and meaningful results.  


# Hypotheses
![Hypotheses](/Figures/hypotheses.png?raw=true "Hypotheses")

# Method
![Base Statistics](/Figures/base_statistics.png?raw=true "Base Statistics")
As shown above, the transformed data still is not quite normal.  Therefore, nonparametric testing seemed more appropriate for the situation.  However, Welch’s t-test was also used for reference for p-values.  As for the nonparametric methods, the Mann-Whitney U test and randomization were used.  For randomization, I shuffled the independent variable such that each individual received a random corresponding dependent variable.  Then the dependent variables were categorized into the aforementioned two groups, and then the test statistic, namely, the difference between means between the two groups, was calculated.  Through ten-thousand iterations, a null distribution for the test statistic was established for the three dependent variables.  

# Results
![p-values](/Figures/p-values.png?raw=true "p-values")
Since the randomization method generates a null distribution of its own, the distribution, along with the test statistic calculated from the original sample, is shown in the figure below.
![Randomization Test](/Figures/random_test.png?raw=true "Randomization Test")

# Conclusion
The difference between the means for CUDIT and CEQ were not significant with respect to the null hypothesis at the alpha level of 0.05.  However, the difference in mean for IDAS was significant with respect to the null hypothesis that asserted no difference.  Taking the hypotheses into consideration, this suggests that subjects in the two groups did not have any statistically significant differences in terms of their views on dependency and PTSD treatment.  In contrast, the heavier smoking group had a significantly lower mean in IDAS score, supporting the potential medicinal benefits of cannabis in terms of mental health.  A recurring trend in cannabis research is the emergence of conflicting results across different studies, and even within this study itself, one may find conflicting results within the interpretation of the effects on cannabis.  The inherent limitations of using numerical analysis for psychiatric study will still remain, but with more resources, studies with stricter controls and methods will be available, leading to tests with increased power and accuracy.  Until then, studies such as this one must first pave the way for future research by contributing to literature using whatever resources available at the time.  

