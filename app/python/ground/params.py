######################################
#   Parameters for App execution
#
#   05.12.2023  Rada
######################################
DB_PRODUCTION = 'db/lazarus.sqlite3'
DB_GROUND = 'db/lazarus_ground.sqlite3'

SCHOOL_NICKS = ['lyceum', '1570']
FORMS = [9, 11]
# SCHOOL_NICKS = ['lyceum']
# FORMS = [9]
# MODELS = ['original', 'standard']
MODELS = ['standard']

SCALES = 8
NUMBER_OF_QUESTIONS = 52  # Number of questions in Questionnaire

# Age range for Wasserman model
AGE_MIN = 14
AGE_MAX = 60

FAKED_RESPONDENTS = 50  # Number of Respondents per Form sample

# Visualization
SHOW_PLOTS = False
SAVE_PLOTS = True
