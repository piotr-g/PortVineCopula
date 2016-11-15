from portvine import *

def test_AD_types():
    # Arrange
    cdf = numpy.array([.1, .2, .3, .4, .5])

    # Act
    ad = AD(cdf)

    # Assert
    assert isinstance(ad, float)
