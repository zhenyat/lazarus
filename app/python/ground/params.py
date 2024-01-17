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

SCALE_NAMES = {
    's1': 'Конфронтационный копинг\t\t',
    's2': 'Дистанцирование\t\t\t',
    's3': 'Самоконтроль\t\t\t',
    's4': 'Поиск социальной поддержки\t',
    's5': 'Принятие ответственности\t',
    's6': 'Бегство-избегание\t\t',
    's7': 'Планирование решения проблемы\t',
    's8': 'Положительная переоценка\t'
}
 
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

### Wasserman scales grouping
# Weights for answers.  Scales:              1             2             3             4             5             6             7             8
CONSTRUCTIVE_WEIGHTS     = [('empty'), (7, 3, 0, 0), (7, 3, 0, 0), (0, 0, 3, 7), (0, 0, 3, 7), (0, 1, 4, 5), (7, 3, 0, 0), (0, 0, 3, 7), (0, 1, 4, 5)]
NON_CONSTRUCTIVE_WEIGHTS = [('empty'), (0, 0, 3, 7), (0, 0, 3, 7), (7, 3, 0, 0), (7, 3, 0, 0), (2, 3, 3, 2), (0, 0, 3, 7), (7, 3, 0, 0), (2, 3, 3, 2)]
REL_CONSTRUCTIVE_WEIGHTS = [('empty'), (7, 3, 0, 0), (7, 3, 0, 0), (2, 2, 3, 3), (2, 2, 3, 3), (0, 0, 3, 7), (7, 3, 0, 0), (2, 2, 3, 3), (0, 0, 3, 7)]

# Visualization
SHOW_PLOTS = True
SAVE_PLOTS = True
TITLES = ['Лицей, 9 кл.', 'Лицей 11 кл.', 'Шк.1570, 9 кл.', 'Шк.1570, 11 кл.']

FIGURE_SIZES = [11, 8]  # inches
TITLE_FONT_SIZE = 20    # fontsize of the figure title
LEGEND_FONT_SIZE = 12   # legend fontsize

# Directories
DATA_FRAMES_DIR = 'db/data_frames/'
HISTOGRAMS_DIR = 'images/histograms/'
SCATTERS_DIR = 'images/scatters/'
MC_DIR = 'images/mc'

# Hypothesis
ALPHA = 0.05