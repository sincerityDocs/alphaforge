from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import os
from dotenv import load_dotenv

load_dotenv()

# Tools
search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()

# Agents
researcher = Agent(
    role='Senior Crypto Researcher',
    goal='Discover promising new memecoins and opportunities early',
    backstory='Expert on-chain analyst and narrative hunter',
    tools=[search_tool],
    verbose=True
)

analyst = Agent(
    role='Technical Analyst',
    goal='Provide accurate technical analysis and risk assessment',
    backstory='Experienced chartist with strong risk management',
    tools=[],
    verbose=True
)

# Tasks and Crew definition here - expand as needed
