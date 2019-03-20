from unittest import TestCase
from Repository.repo import RepoData
from errors.Errors import RepoError

class TestRepoData(TestCase):
    def setUp(self):
        self.repo = RepoData()

    def test_add(self):
        self.repo.add(1)
        self.repo.add('papa')
        self.assertEqual(len(self.repo), 2)
        self.assertRaises(RepoError, self.repo.add, 1)
        self.assertRaises(RepoError, self.repo.add, 'papa')


    def test_remove(self):
        self.repo.add(1)
        self.repo.add('papa')
        self.repo.remove(1)
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.remove, 8888)


    def test_getAll(self):
        self.repo.add(1)
        self.repo.add('papa')
        self.assertEqual(2, len(self.repo))
