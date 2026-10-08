# PostgreSQL DB Setup

Run the following bash commands to setup the neon PostgreSQL required environment variables

## WINDOWS

in an adminstrator terminal run:

```
setx ALEKS_DB_URL "postgresql://neondb_owner:npg_cVOowHj6NuI1@ep-dark-union-b2fckmdf.c-6.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require" /M
```

```
setx ALEKS_DB_POOLED "postgresql://neondb_owner:npg_cVOowHj6NuI1@ep-dark-union-b2fckmdf-pooler.c-6.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require" /M
```
