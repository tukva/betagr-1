import sqlalchemy as sa

metadata = sa.MetaData()

tb_real_team = sa.Table(
    'tb_real_team', metadata,
    sa.Column('real_team_id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(80), nullable=False, unique=True),
    sa.Column('created_on', sa.DateTime(), nullable=False))

tb_team = sa.Table(
    'tb_team', metadata,
    sa.Column('team_id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(80), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=False),
    sa.Column('site_name', sa.String(25), nullable=False),
    sa.Column('real_team_id', sa.Integer, sa.ForeignKey('tb_real_team.real_team_id')))