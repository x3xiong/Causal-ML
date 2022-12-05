from .regression import synthetic_data
from .regression import simulate_nuisance_and_easy_treatment
from .regression import simulate_randomized_trial
from .regression import simulate_easy_propensity_difficult_baseline
from .regression import simulate_unrelated_treatment_control
from .regression import simulate_hidden_confounder
from .classification import make_uplift_classification

from .synthetic import get_synthetic_preds, get_synthetic_preds_holdout
from .synthetic import get_synthetic_summary, get_synthetic_summary_holdout
from .synthetic import scatter_plot_summary, scatter_plot_summary_holdout
from .synthetic import bar_plot_summary, bar_plot_summary_holdout
from .synthetic import distr_plot_single_sim
from .synthetic import scatter_plot_single_sim
from .synthetic import get_synthetic_auuc