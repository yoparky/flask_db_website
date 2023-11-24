# To actually have your app use this file, you need to RENAME the file to db_credentials.py
# You will find details about your CS340 database credentials on Canvas.

# the following will be used by the webapp.py to interact with the database
# You can also use environment variables

# For Local Devlelopment
# host = 'localhost'
# user = 'root'                                   # can be different if you set up another username in your MySQL installation
# passwd = 'nottellingyou'                        # set accordingly
# db = 'bsg'

# For OSU Flip Servers
# host = 'classmysql.engr.oregonstate.edu'
# user = 'cs340_parky8'
# passwd = '2188' 
# db = 'cs340_parky8'

# For Amazon RDS
host = 'osu-project-db.cquzhqqutqv3.us-east-2.rds.amazonaws.com'          # Endpoint provided by Amazon RDS
user = 'admin'          # Username for RDS instance
passwd = 'password'        # Password for RDS instance
db = 'OSU_Project'       # Database name