import  pyspec
from pub_sub import stable

PUB_SUB = stable.event('CLI test')

TEST = pyspec.describe('this is a test', None, PUB_SUB)

TEST.it('can pass', 1).should.eq(1)
TEST.it('can fail', 1).should.eq(2)

PUB_SUB.topic('runner').pub(pyspec.runner())
PUB_SUB.topic('run requested').pub(False)
