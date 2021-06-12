from dataclasses import dataclass

@dataclass
class Dataset(object):

    context: str
    fname: str
    train: object # train.csv -> DF(dataFramework) 로 전환된 객체
    test: object # test.csv 가 DF 로 전환된 객체
    id: str # 승객 ID로 문제가 된다
    label: str # 승객ID에 따른 생존여부

    # 데이터를 읽고(getter = 프로퍼티)
    # 쓰기(setter) 기능을 추가한다.

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def train(self) -> str: return self._train

    @train.setter
    def train(self, fname): self._train = train


    @property
    def fname(self) -> str: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    @property
    def test(self) -> str: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @context.setter
    def label(self, label): self._label = label