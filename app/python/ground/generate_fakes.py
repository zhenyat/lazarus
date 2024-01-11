#! /usr/bin/env python3

###############################################################################
#   Executable module to generate fakes for tables:
#       Respondents, Responses, Scores
#
#   05.12.2023  Rada Telyukova. HSE Lyceum
###############################################################################
from params import DB_GROUND
import db
import respondents
import responses
import scores

def main():
    conn = db.create_connection(DB_GROUND)
    
    respondents.populate_with_fakes(conn)
    responses.populate_with_fakes(conn)
    scores.populate_with_fakes(conn)

if __name__ == '__main__':
    main()
