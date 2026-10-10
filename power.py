
from fastapi import APIRouter, Depends, Query
from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.database import get_db

router = APIRouter(prefix="/api/power", tags=["Power Generation"])


@router.get("/history")
def get_power_history(
    limit: int = Query(default=100, ge=1, le=1000),
    db: Session = Depends(get_db)
):
    query = text("""
        SELECT
            id,
            timestamp,
            plant_id,
            ac_power,
            dc_power,
            daily_yield,
            total_yield,
            source
        FROM power_generation
        ORDER BY timestamp DESC
        LIMIT :limit
    """)

    result = db.execute(query, {"limit": limit})

    records = []
    for row in result.mappings():
        record = dict(row)
        if record.get("timestamp") is not None:
            record["timestamp"] = record["timestamp"].isoformat()
        records.append(record)

    return {
        "count": len(records),
        "data": records
    }
