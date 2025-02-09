"""Create users, albums, and tracks tables

Revision ID: 4ca319402cf5
Revises: 
Create Date: 2025-01-27 23:21:04.369209

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4ca319402cf5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('artist', sa.String(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('aoty_score', sa.Integer(), nullable=True),
    sa.Column('cover_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.Column('aoty_score', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artists_id'), 'artists', ['id'], unique=False)
    op.create_table('tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('artist', sa.String(), nullable=False),
    sa.Column('album', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.Column('aoty_score', sa.Integer(), nullable=True),
    sa.Column('audio_features', postgresql.JSON(astext_type=sa.Text()), nullable=False),
    sa.Column('cover_url', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tracks_id'), 'tracks', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('album_compatibilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_1', sa.Integer(), nullable=False),
    sa.Column('user_id_2', sa.Integer(), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('compatibility_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['user_id_1'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id_2'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_album_compatibilities_id'), 'album_compatibilities', ['id'], unique=False)
    op.create_table('artist_compatibilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_1', sa.Integer(), nullable=False),
    sa.Column('user_id_2', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('compatibility_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['user_id_1'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id_2'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_artist_compatibilities_id'), 'artist_compatibilities', ['id'], unique=False)
    op.create_table('compatibilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_1', sa.Integer(), nullable=False),
    sa.Column('user_id_2', sa.Integer(), nullable=False),
    sa.Column('compatibility_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id_1'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id_2'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_compatibilities_id'), 'compatibilities', ['id'], unique=False)
    op.create_table('recommendations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('album', sa.Integer(), nullable=False),
    sa.Column('recommendation_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['album'], ['albums.id'], ),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_recommendations_id'), 'recommendations', ['id'], unique=False)
    op.create_table('track_compatibilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_1', sa.Integer(), nullable=False),
    sa.Column('user_id_2', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.Integer(), nullable=False),
    sa.Column('compatibility_score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.ForeignKeyConstraint(['user_id_1'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id_2'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_track_compatibilities_id'), 'track_compatibilities', ['id'], unique=False)
    op.create_table('track_listening_histories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('track_id', sa.String(), nullable=False),
    sa.Column('play_count', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'track_id', name='uq_user_track')
    )
    op.create_index(op.f('ix_track_listening_histories_id'), 'track_listening_histories', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_track_listening_histories_id'), table_name='track_listening_histories')
    op.drop_table('track_listening_histories')
    op.drop_index(op.f('ix_track_compatibilities_id'), table_name='track_compatibilities')
    op.drop_table('track_compatibilities')
    op.drop_index(op.f('ix_recommendations_id'), table_name='recommendations')
    op.drop_table('recommendations')
    op.drop_index(op.f('ix_compatibilities_id'), table_name='compatibilities')
    op.drop_table('compatibilities')
    op.drop_index(op.f('ix_artist_compatibilities_id'), table_name='artist_compatibilities')
    op.drop_table('artist_compatibilities')
    op.drop_index(op.f('ix_album_compatibilities_id'), table_name='album_compatibilities')
    op.drop_table('album_compatibilities')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tracks_id'), table_name='tracks')
    op.drop_table('tracks')
    op.drop_index(op.f('ix_artists_id'), table_name='artists')
    op.drop_table('artists')
    op.drop_table('albums')
    # ### end Alembic commands ###
