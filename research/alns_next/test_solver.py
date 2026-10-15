import copy
import json
from pathlib import Path
import unittest
from alns_solver import Solver
from validate import validate

DATA=json.loads(Path(__file__).with_name('instances.json').read_text())


class Tests(unittest.TestCase):
    def test_separator_removal_and_repair_preserve_tasks(self):
        s=Solver(DATA['cases']['Case1'],3,41)
        r=s.repair([[],[],[]],list(range(s.n)),1)
        for mode in range(4):
            for _ in range(8):
                part,removed=s.destroy(r,mode)
                self.assertTrue(all(s.valid(x) for x in part))
                self.assertEqual(sorted([u for x in part for u in x]+removed),list(range(s.n)))
                for repair in range(2):
                    out=s.repair(part,removed,repair)
                    if out is None:continue
                    out=s.intensify(out,20)
                    self.assertTrue(all(s.valid(x) for x in out))
                    self.assertEqual(sorted(u for x in out for u in x),list(range(s.n)))
                    self.assertEqual(len(out),3)

    def test_validator_rejects_duplicate_and_wrong_times(self):
        s=Solver(DATA['cases']['Case1'],3)
        result=s.solve(30,2);result['case']='Case1'
        validate(DATA,result)
        bad=copy.deepcopy(result)
        r=bad['best_makespan']['routes'];r[0][0]=r[1][0]
        with self.assertRaises(ValueError):validate(DATA,bad)
        bad=copy.deepcopy(result);bad['best_makespan']['Tmax']=8
        with self.assertRaises(ValueError):validate(DATA,bad)
        self.assertEqual(result['status'],'UNKNOWN')

    def test_same_location_tasks_not_consecutive(self):
        s=Solver({'points':[{'id':1,'x':1,'y':0,'visits':3},{'id':2,'x':2,'y':0,'visits':1}],
                  'speed_kmh':55,'unit_km':.1,'service_h':5/60,'limit_h':9},1)
        self.assertFalse(s.valid([0,1]))
        self.assertTrue(s.valid([0,3,1]))
        self.assertIsNone(s.repair([[0,3,1]],[2],1))


if __name__=='__main__':unittest.main()
