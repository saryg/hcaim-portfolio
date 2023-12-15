import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import patsy.contrasts as contr
import math

# plots
def plot_hist_and_norm_pdf(v, standardize=False, bins=10):
    m = v.mean()
    s = v.std()
    
    if (standardize):
        v = (v - m)/s
        m = 0
        s = 1
        
    plt.hist(v, density=True, bins=bins)

    x = np.linspace(min(v), max(v), 100)
    plt.plot(x, ss.norm.pdf(x, loc=m, scale=s), 'r-')

def pc_over_2sd(v):
    m = v.mean(); s = v.std()
    return sum((v > (m + 2 * s)) | (v < (m - 2 * s)))/len(v)*100


# implementation of statistical methods
def get_outlier_cv(sample_size):
    return ss.norm.ppf(0.9995) if sample_size > 80 else ss.norm.ppf(0.995)

def scale(v):
    return (v - v.mean()) / v.std()

def code_alpha(v, b):
    coding = contr.Treatment(reference=b).code_without_intercept(sorted(list(v.unique())))
    return coding, [b] + list(np.char.strip(np.array(coding.column_suffixes), "[.T]"))

def code_levels(levels):
    coding = contr.Treatment(reference=levels[0]).code_without_intercept(levels)
    return coding
        
# computation of statistics
def se_skew(n):
    return math.sqrt(6*n*(n-1)/(n-2)/(n+1)/(n+3))

def se_kurt(n):
    return se_skew(n)*2*math.sqrt((n-1)*(n+1)/(n-3)/(n+5))

def t_df(g1, g2, equal_var=True):
    g1_n = len(g1); g2_n = len(g2)
    if (equal_var):
        return g1_n + g2_n - 2;

    g1_var = g1.var(); g2_var = g2.var()
    return (g1_var/g1_n + g2_var/g2_n)**2 / ((g1_var/g1_n)**2/(g1_n - 1) + (g2_var/g2_n)**2/(g2_n - 1))

def chi2_df(r, c):
    return min(r-1, c-1)

def t_es_d(g1, g2):
    g1_n = len(g1); g2_n = len(g2)
    return (g1.mean() - g2.mean()) / math.sqrt(((g1_n - 1) * g1.var() + (g2_n -1) * g2.var()) / (g1_n + g2_n - 2))

def mwu_es_r(g1, g2):
    g1_n = len(g1); g2_n = len(g2)
    return 1 - 2 * ss.mannwhitneyu(g1, g2).statistic/len(g1)/len(g2)
    
def mwu_es_auc(g1, g2):
    return ss.mannwhitneyu(g1, g2).statistic/len(g1)/len(g2)

def wsr_es_r(g1, g2):
    n = len(g1)
    return 2 * ss.wilcoxon(g1, g2).statistic/n/(n+1)

def anova_es_n2(f, n, k):
    return 1/(1 + (n-k)/f/(k-1))

def kw_es_n2(H, n, k):
    return (H - k + 1)/(n-k)

def f_es_w(Q, n, k):
    return Q/n/(k-1)

def chi2_es_v(X2, n, r, c):
    return math.sqrt(X2/n/chi2_df(r, c))

def mn_es_g(b, c):
    return max(b, c)/(b+c) - 0.5

effects = {
    'lvls_4': ['large', 'medium', 'small', 'negligible'],
    'lims_r': [[.5, .3, .1, 0]],
    'lims_w': [[.5, .3, .1, 0]],
    'lims_d': [[.8, .5, .2, 0]],
    'lims_e': [[.14, .06, .01, 0]],
    'lims_g': [[0.25, 0.15, 0.05, 0]],
    'lims_v': [[0.50, 0.30, 0.10, 0], 
               [0.35, 0.21, 0.07, 0], 
               [0.29, 0.17, 0.06, 0], 
               [0.25, 0.15, 0.05, 0], 
               [0.22, 0.13, 0.04, 0]]
}
                     
def magnitude(statistic, value, index=0):
    limits = effects['lims_' + statistic][index]
    levels = effects['lvls_' + str(len(limits))]
    for i, l in enumerate(limits):
        if abs(value) >= l:
            return levels[i]

def chi2_magnitude_index(r, c):
    return chi2_df(r, c) - 1

# formatting
def pval_str(number):
    return str("{:.3f}".format(number)).replace("-0", "-").lstrip("0")

def print_stat(name, value):
    print(str(name) + ": " + str(value))
    
    
