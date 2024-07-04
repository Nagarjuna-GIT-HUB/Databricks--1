# Databricks notebook source
# MAGIC %sql
# MAGIC --create database super11;
# MAGIC create table super11.india (id int , name string , salary int);
# MAGIC insert into super11.india values(1,'dravid',1000);
# MAGIC select * from super11.india;
# MAGIC --update super11.india set salary= salary+1000;
# MAGIC -- select * from super11.india;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from super11.india;

# COMMAND ----------

# MAGIC %sql
# MAGIC update super11.india set salary= salary+1000;
# MAGIC  select * from super11.india;
