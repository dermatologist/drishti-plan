
* change database uri in config.py



    db                  Perform database migrations
    shell               Runs a Python shell inside Flask application context.
    runserver           Runs the Flask development server i.e. app.run()





usage: Perform database migrations

Perform database migrations

manage.py db <option>

positional arguments:
  {init,revision,migrate,edit,merge,upgrade,downgrade,show,history,heads,branches,current,stamp}
    init                Creates a new migration repository
    revision            Create a new revision file.
    migrate             Alias for 'revision --autogenerate'
    edit                Edit current revision.
    merge               Merge two revisions together. Creates a new migration
                        file
    upgrade             Upgrade to a later version
    downgrade           Revert to a previous version
    show                Show the revision denoted by the given symbol.
    history             List changeset scripts in chronological order.
    heads               Show current available heads in the script directory
    branches            Show current branch points
    current             Display the current revision for each database.
    stamp               'stamp' the revision table with the given revision;
                        don't run any migrations