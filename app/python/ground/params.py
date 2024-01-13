##############################################
#   Parameters for Faked Data generation
#
#   05.12.2023  Rada Telyukova
#   13.01.2024  Last update
##############################################
from termcolor import colored

DB_PRODUCTION = 'db/lazarus.sqlite3'
DB_GROUND = 'db/lazarus_ground.sqlite3'

SCALES = 8
SCALE_NAMES_LOCALIZED = [
    'Конфронтационный копинг',
    'Дистанцирование',
    'Самоконтроль',
    'Поиск социальной поддержки',
    'Принятие ответственности',
    'Бегство-избегание',
    'Планирование решения проблемы',
    'Положительная переоценка'
] 

NUMBER_OF_QUESTIONS = 52  # Number of questions in Questionnaire
ANSWERS = ['never', 'rarely', 'sometimes', 'regularly']
ORIGINAL_POINTS = [0, 1, 2, 3]

# Age range for Wasserman model
AGE_MIN = 14
AGE_MAX = 60

FAKED_RESPONDENTS = 50  # Number of Respondents per Form sample

UNIFORM_RANDOM_MODE = False
SCHOOL_NICKS = ['lyceum', '1570']
FORMS = [9, 11]
# MODELS = ['original', 'standard']
MODELS = ['standard']

# ANSWERS_GENERATION_MODE = 'uniform'
# SCHOOL_NICKS = ['1570']
# FORMS = [11]
# MODELS = ['standard']

# ANSWERS_GENERATION_MODE = 'strong'
# SCHOOL_NICKS = ['1570']
# FORMS = [11]
# MODELS = ['standard']

# ANSWERS_GENERATION_MODE = 'weak'    # {'uniform' | 'strong' | 'weak'}
# SCHOOL_NICKS = ['1570']
# FORMS = [9]
# MODELS = ['standard']

# Weights for answers. Scales:         1             2             3             4             5             6             7             8
# STRONG_WEIGHTS = [('empty'), (4, 3, 2, 1), (1, 2, 3, 4), (1, 2, 3, 4), (1, 2, 3, 4), (1, 2, 3, 4), (4, 4, 4, 1), (1, 2, 3, 4), (1, 4, 4, 1)]
# WEAK_WEIGHTS   = [('empty'), (1, 2, 3, 4), (1, 3, 4, 2), (4, 3, 2, 1), (4, 3, 2, 1), (4, 3, 2, 1), (1, 2, 3, 4), (4, 4, 1, 1), (4, 1, 1, 4)]

# STRONG_WEIGHTS = [('empty'), (5, 4, 1, 0), (0, 1, 4, 5), (0, 1, 4, 5), (0, 1, 4, 5), (0, 1, 4, 5), (1, 4, 4, 1), (0, 1, 4, 5), (1, 4, 4, 1)]
# WEAK_WEIGHTS   = [('empty'), (0, 1, 4, 5), (5, 4, 1, 0), (5, 4, 1, 0), (5, 4, 1, 0), (5, 4, 1, 0), (4, 1, 1, 4), (5, 4, 1, 0), (4, 1, 1, 4)]

# Wasserman scales grouping
#                   Scales:                  1             2             3             4             5             6             7             8
CONSTRUCTIVE_WEIGHTS     = [('empty'), (7, 3, 0, 0), (7, 3, 0, 0), (0, 0, 3, 7), (0, 0, 3, 7), (0, 1, 4, 5), (7, 3, 0, 0), (0, 0, 3, 7), (0, 1, 4, 5)]
NON_CONSTRUCTIVE_WEIGHTS = [('empty'), (0, 0, 3, 7), (0, 0, 3, 7), (7, 3, 0, 0), (7, 3, 0, 0), (2, 3, 3, 2), (0, 0, 3, 7), (7, 3, 0, 0), (2, 3, 3, 2)]
REL_CONSTRUCTIVE_WEIGHTS = [('empty'), (7, 3, 0, 0), (7, 3, 0, 0), (2, 2, 3, 3), (2, 2, 3, 3), (0, 0, 3, 7), (7, 3, 0, 0), (2, 2, 3, 3), (0, 0, 3, 7)]

# Visualization
SHOW_PLOTS = True
SAVE_PLOTS = True
FIGURE_SIZES = [11, 8] # inches

# Directories
DATA_FRAMES_DIR = 'db/data_frames/'
HISTOGRAMS_DIR = 'images/histograms/'
SCATTERS_DIR = 'images/scatters/'
MC_DIR = 'images/mc'
