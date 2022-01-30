"""A list of all BigQuery SQL key words."""

# https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#reserved_keywords
bigquery_reserved_keywords = """ALL
AND
ANY
ARRAY
AS
ASC
ASSERT_ROWS_MODIFIED
AT
BETWEEN
BY
CASE
CAST
COLLATE
CONTAINS
CREATE
CROSS
CUBE
CURRENT
DEFAULT
DEFINE
DESC
DISTINCT
ELSE
END
ENUM
ESCAPE
EXCEPT
EXCLUDE
EXISTS
EXTRACT
FALSE
FETCH
FOLLOWING
FOR
FROM
FULL
GROUP
GROUPING
GROUPS
HASH
HAVING
IF
IGNORE
IN
INCLUDE
INNER
INTERSECT
INTERVAL
INTO
IS
JOIN
LATERAL
LEFT
LIKE
LIMIT
LOOKUP
MERGE
NEW
NO
NOT
NULL
NULLS
OF
ON
OR
ORDER
OUTER
OVER
PARTITION
PIVOT
PRECEDING
PROTO
RANGE
RECURSIVE
RESPECT
RIGHT
ROLLUP
ROWS
SELECT
SET
SOME
STRUCT
TABLESAMPLE
THEN
TO
TREAT
TRUE
UNBOUNDED
UNION
UNNEST
UNPIVOT
USING
WHEN
WHERE
WINDOW
WITH
WITHIN"""

# Note BigQuery doesn't have a list of Unreserved Keywords
# so these are just ones we need to allow parsing to work
bigquery_unreserved_keywords = """ACCOUNT
ADD
ADMIN
AFTER
ALTER
APPLY
AUTO_INCREMENT
BEGIN
BERNOULLI
BINARY
BINDING
CACHE
CASCADE
CHAIN
CHARACTER
CHECK
CLUSTER
COLUMN
COMMENT
COMMIT
CONCURRENTLY
CONNECT
CONSTRAINT
COPY
CURRENT_USER
CYCLE
DATA
DATABASE
DATE
DATEADD
DATETIME
DECLARE
DELETE
DESCRIBE
DETERMINISTIC
DOMAIN
DOUBLE
DROP
EXECUTE
EXECUTION
EXPLAIN
EXTENSION
EXTERNAL
FILE
FILTER
FIRST
FOREIGN
FORMAT
FUNCTION
FUTURE
GRANT
GRANTED
GRANTS
HOUR
ILIKE
IMPORTED
INCREMENT
INDEX
INSERT
INTEGRATION
KEY
LANGUAGE
LARGE
LAST
MANAGE
MASKING
MATERIALIZED
MAXVALUE
MINUS
MINVALUE
ML
MODEL
MODIFY
MONITOR
NAME
NAN
NOCACHE
NOCYCLE
NOORDER
OBJECT
OFFSET
OPERATE
OPTION
OPTIONS
ORDINAL
OVERLAPS
OVERWRITE
OWNERSHIP
PERCENT
PIPE
POLICY
PRECISION
PRIMARY
PRIOR
PRIVILEGES
PROCEDURE
PUBLIC
QUALIFY
QUARTER
READ
REFERENCE_USAGE
REFERENCES
RENAME
REPEATABLE
REPLACE
RESOURCE
RESTRICT
RETURNS
REVOKE
RLIKE
ROLE
ROLLBACK
ROW
ROUTINE
SCHEMA
SCHEMAS
SECOND
SEPARATOR
SERVER
SEQUENCE
SESSION_USER
SHARE
STAGE
START
STREAM
SYSTEM
SYSTEM_TIME
TABLE
TABLESPACE
TASK
TEMP
TEMPORARY
TIME
TIMESTAMP
TRANSACTION
TRANSIENT
TRIGGER
TRUNCATE
TYPE
UNIQUE
UNSIGNED
UPDATE
USAGE
USE
USE_ANY_ROLE
USER
VALUE
VALUES
VARYING
VERSION
VIEW
WAREHOUSE
WITHOUT
WORK
WRAPPER
WRITE
ZONE"""
