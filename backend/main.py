from fastapi import FastAPI
from typing import List, Dict
from tools.historical_data_tool import historical_data_tool_func
from tools.orchestrator import get_orchestrator_response

app = FastAPI()

@app.get("/orchestrator/{user_query}")
def get_orchestrator_output(user_query: str) -> dict[str,str]:
    response = get_orchestrator_response(user_query)
    return {
        "debug_info": response["debug_info"],
        "llm_response": response["llm_response"]
    }

@app.get("/historical_prices/{user_query}")
def get_historical_prices(user_query: str) -> dict[str,str]:
    """
    Fetch historical price data.

    Example of a user query: "What was the difference in the average price between detached and terraced houses in January 2024?"
    """    
    response = historical_data_tool_func(user_query)

    return {
        "debug_info": response["debug_info"],
        "llm_response": response["llm_response"]
    }


@app.get("/current_listings")
def get_current_listings() -> List[Dict]:
    """
    Fetch the current listings available.
    """
    return None


@app.get("/journey_planner")
def get_journey_planner(origin: str, destination: str) -> Dict:
    """
    Get journey details between origin and destination.
    """
    # You can add real journey planning logic here
    return None


@app.get("/top_locations")
def get_top_locations() -> List[Dict]:
    """
    Fetch the top-rated locations.
    """
    return None