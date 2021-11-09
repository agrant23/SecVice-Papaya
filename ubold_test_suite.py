import unittest
import ubold_test_cases as test_case

suite = unittest.TestSuite()
suite.addTest(test_case.AccountCreation("test_account_creation"))
suite.addTest(test_case.AccountCreation("test_user_account_page"))
suite.addTest(test_case.Scope("test_scope_object_creation"))
suite.addTest(test_case.Scope("test_scope_object_creation"))
suite.addTest(test_case.Scope("test_scope_object_creation"))
suite.addTest(test_case.SignIn("test_sign_in_link"))
suite.addTest(test_case.SignIn("test_ubold_logo_sign_in_link"))

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite)
