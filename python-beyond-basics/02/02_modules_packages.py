# Databricks notebook source
# MAGIC %md
# MAGIC 1. Each .py file is module in python.
# MAGIC 2. Module is object of class "module"
# MAGIC 3. Use keyword "import" to use the functinality within the module
# MAGIC 4. Python checks the sys.path for module

# COMMAND ----------

import sys
from pprint import pprint
print(type(sys))
pprint(sys.path)

# COMMAND ----------

from bovine import common

# COMMAND ----------

# MAGIC %sh
# MAGIC ls

# COMMAND ----------

from bovine import common

# COMMAND ----------

common.ruminate()

# COMMAND ----------

from bovine import ox

# COMMAND ----------


