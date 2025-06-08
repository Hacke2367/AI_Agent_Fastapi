from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from langgraph_app.graph_builder import run_graph



app = FastAPI(
title="Cross-Sell & Upsell Recommendation API",
    description="LangGraph agent pipeline that returns research report and recommendations."
)

@app.get("/recommendation")
def get_recommedation(customer_id: str):
    try:
        output = run_graph(customer_id)
        return JSONResponse(
            content={
                "success": True,
                "customer_id": customer_id,
                "research_report": output["research_report"],
                "recommendations": output["recommendations"]
            },
            status_code=200
        )
    except ValueError as ve:
        return JSONResponse(
            content={"success": False, "error": str(ve)},
            status_code=404
        )
    except Exception as e:
        print(f"[ERROR] Internal Server Error: {e}")
        return JSONResponse(
            content={"success": False, "error": f"Internal error: {str(e)}"},
            status_code=500
        )
