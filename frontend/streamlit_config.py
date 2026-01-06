import streamlit as st
from datetime import datetime
import requests
import pandas as pd

from pyreusables.configs.credentials import credentials
from pyreusables.utilities import pylogger as logger

# Local API configurations
api_host = credentials.LOCAL_API_HOST + "/expenses/"
