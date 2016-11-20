import unittest
import trunk
import branch


trunk_tests = unittest.TestLoader().loadTestsFromModule(trunk)
trunk_results = unittest.TestResult()
trunk_tests.run(trunk_results)

branch_tests = unittest.TestLoader().loadTestsFromModule(branch)
branch_results = unittest.TestResult()
branch_tests.run(branch_results)

for test_name in trunk_results.results.keys():
    if trunk_results.results[test_name] != branch_results.results[test_name]:
        print('Trunk test "%s" result is %s, when branch result for the same test is %s' % (test_name, trunk_results.results[test_name], branch_results.results[test_name]))
