import random

from app.core.database import Base, SessionLocal, engine
from app.models.resource import Resource

TYPES = ["EC2_INSTANCE", "RDS_DATABASE", "S3_BUCKET", "EBS_VOLUME", "LOAD_BALANCER"]
REGIONS = ["us-east-1", "us-west-2", "eu-west-1", "ap-south-1"]


def seed() -> None:
    random.seed(42)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with SessionLocal() as db:
        for i in range(1, 31):
            rtype = random.choice(TYPES)
            wasteful = random.random() < 0.4
            db.add(
                Resource(
                    resource_id=f"{rtype[:3].lower()}-{1000 + i}",
                    name=f"{rtype.lower().replace('_', '-')}-{i}",
                    resource_type=rtype,
                    region=random.choice(REGIONS),
                    monthly_cost_usd=round(random.uniform(20, 400), 2),
                    cpu_utilization=round(
                        random.uniform(1, 9) if wasteful else random.uniform(30, 90), 1
                    ),
                    idle_days=random.randint(10, 30) if wasteful else random.randint(0, 3),
                    status="ACTIVE",
                )
            )
        db.commit()
    print("Seeded 30 resources")


if __name__ == "__main__":
    seed()