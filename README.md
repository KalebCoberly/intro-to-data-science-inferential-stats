# Intro to Data Science: Inferential Stats
### Abstract
Do incongruent stimuli slow responses? To get at this question, I used dubious data to simulate a one-tailed, dependent-samples t-test comparing response times in a classic Stroop task. The results from the congruent word task (M = 14.05, SD = 3.56) and the incongruent word task (M = 22.02, SD = 4.80) suggest that incongruent stimuli increase response times in the Stroop task, t(23) = 8.021, p < .001. The sample size, 24, is too small to warrant drawing conclusions without further research. And, because of the small sample size, I ignored the assumptions regarding sample variances and distribution of differences required for a valid t-test.

### Background
In a Stroop task, participants iterate through two equally lengthed lists of color names. Each color name is printed in a color of ink. In the first list, the congruent condition, words are printed in the same color that is named by the word. In the second list, the incongruent condition, words are printed in a color that is incongruent with the named color. Participants must name the color of the ink, regardless of the color that the word indicates, as fast as possible before moving on to the next word.

Researchers measure the response times and compare those of the congruent condition with those of the incongruent condition.

### Data
The CSV file ('stroopdata.csv') contains observations from 24 participants: the total reponse time to the congruent list and the total response time to the incongruent list; i.e., there are two, dependent samples of size 24 each.

This data comes from Udacity and may or may not be simulated.