from dagster import (
    AssetSelection,
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    FilesystemIOManager,  # Update the imports at the top of the file to also include this
    EnvVar,
)

from . import assets
from dagster_duckdb_pandas import DuckDBPandasIOManager
from .resources import DataGeneratorResource

all_assets = load_assets_from_modules([assets])

# Define a job that will materialize the assets
hackernews_job = define_asset_job("hackernews_job", selection=AssetSelection.all())

# Addition: a ScheduleDefinition the job it should run and a cron schedule of how frequently to run it
hackernews_schedule = ScheduleDefinition(
    job=hackernews_job,
    cron_schedule="0 * * * *",  # every hour
)

io_manager = FilesystemIOManager(
    base_dir="data",  # Path is built relative to where `dagster dev` is run
)

database_io_manager = DuckDBPandasIOManager(database="analytics.hackernews")

num_days = EnvVar.int("HACKERNEWS_NUM_DAYS_WINDOW")
datagen = DataGeneratorResource(num_days=num_days)  # Make the resource

defs = Definitions(
    assets=all_assets,
    schedules=[hackernews_schedule],
    resources={
        "io_manager": io_manager,
        "database_io_manager": database_io_manager,
        "hackernews_api": datagen,  # Add the newly-made resource here
    },
)