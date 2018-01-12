# -*- coding: utf-8 -*-
import doctest
import logging

log = logging.getLogger(__name__)


def pytest_addoption(parser):
    group = parser.getgroup('doctest-ellipsis-markers')
    group.addoption(
        '--doctest-ellipsis-markers',
        action='store',
        dest='doctest_ellipsis_markers',
        default='',
        help='Set additional value interpreted as '
             'ELLIPSIS_MARKER in expectations.'
    )
    parser.addini(
        'doctest_ellipsis_markers', 'additional ELLIPSIS_MARKER replacements',
        type="args", default=['[...]', "'...'", '"..."']
    )


OutputChecker = doctest.OutputChecker


class ExtendedOutputChecker(doctest.OutputChecker):
    """Will match '...' as a whole line

    https://stackoverflow.com/a/5820975/260480
    """
    additional_ellipsis_markers = ["'...'"]

    def check_output(self, want, got, optionflags):
        if optionflags & doctest.ELLIPSIS:
            # raise Exception(want)
            for maker in self.additional_ellipsis_markers:
                want = want.replace(maker, "...")
        return OutputChecker.check_output(self, want, got, optionflags)


doctest.OutputChecker = ExtendedOutputChecker


def pytest_configure(config):
    option_markers = config.option.doctest_ellipsis_markers
    if option_markers:
        ExtendedOutputChecker.additional_ellipsis_markers = option_markers
    else:
        ini_markers = config.getini("doctest_ellipsis_markers")
        ExtendedOutputChecker.additional_ellipsis_markers = ini_markers
