import pandas
from scipy import stats
import math

def print_results(df, alpha, units='seconds.'):
    '''Prints results of a right-tailed, t-test with dependent samples,
    along with Cohen's d, r-squared, and a confidence interval.

    Dataframe must have two columns, condition one and condition two.

    Parameters:
        df: pandas.DataFrame of sample data. Two columns, condition one and
        condition two.
        alpha: floating point to determine confidence level.
        units: (optional) string to print outcome units. End with period.
            Default: 'seconds.'
    '''
    retain_null = True
    cond_1, cond_2 = df.columns
    
    # Confidence level
    print('alpha:', alpha)

    # t-critical value for a right-tailed test
    # (dependent sample, dof = N-1)
    desc = df.describe()
    dof = desc.loc['count',cond_2]-1
    t_critical = stats.t.ppf(q=1-alpha, df=dof) #3.485
    print('Critical t-value:', round(t_critical, 3), '\n')

    # Difference of means
    diff_of_means = desc.loc['mean', cond_2] \
                    - desc.loc['mean', cond_1]

    # Sample differences
    samp_diffs_sr = df[cond_2] - df[cond_1]

    # Standard Error of differences
    SE = (samp_diffs_sr.std() / math.sqrt(desc.loc['count', cond_2]))

    # # t statistic = mean of condition one minus mean of condition 2,
    # # divided by standard error.
    # t_stat = diff_of_means / SE
    
    t_stat, p_val = stats.ttest_rel(df[cond_1], df[cond_2])
    t_stat = abs(t_stat)
    p_val = p_val / 2

    # Retain or reject the null hypothesis.
    if t_stat > t_critical:
        retain_null = False
        print('Reject the null hypothesis.')
        print('t(', dof, '):', round(t_stat, 3))
        print('p =', p_val)
        print('p <', alpha, '\n')

        # Cohen's d
        cohens_d = diff_of_means / desc.loc['std', cond_2]
        print('The treatment condition had an effect of changing \
the mean outcome by', round(cohens_d, 2), 'standard deviations \
(Cohen\'s d), or', round(diff_of_means, 4), units, '\n')

        # r-squared
        r_squared = t_stat**2 / (t_stat**2 + dof)
        print('The treatment likely accounts for',
              '{:.1%}'.format(r_squared),
              'of the difference in outcomes.\n')

        # Confidence interval
        ME =  stats.t.ppf(q=1-alpha/2, df=df) * SE
        con_lvl = 1 - alpha
        print('We can say with', '{:.1%}'.format(con_lvl),
              'confidence that conducting the treatment will result \
in mean outcome differences between',
              round((diff_of_means - SE), 4), 'and',
              round((diff_of_means + SE), 4), units)
              
    else:
        print('Retain the null hypothesis.')
        print('t(', dof, '):', round(t_stat, 3), '\n')
        print('p =', p_val, '\n')
        print('p >', alpha, '\n')
    
    return retain_null