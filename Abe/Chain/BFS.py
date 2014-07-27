# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .Sha256Chain import Sha256Chain

class BFS(Sha256Chain):
    def __init__(chain, **kwargs):
        chain.name = 'Bitfrog Share'
        chain.code3 = 'BFS'
        chain.address_version = '\x00'
        chain.magic = '\xfb\xc0\xb6\xdb'
        Sha256Chain.__init__(chain, **kwargs)

    def ds_parse_block_header(chain, ds):
        d = Sha256Chain.ds_parse_block_header(chain, ds)
        d['generationSignature'] = ds.read_bytes(32)
        d['baseTarget'] = ds.read_int64()
        d['cumulativeDifficulty'] = ds.read_bytes(ds.read_compact_size())
        return d
		
    def ds_block_header_hash(chain, ds):
        return chain.block_header_hash(
            ds.input[ds.read_cursor : ds.read_cursor + 120])
