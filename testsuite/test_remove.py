# test_remove.py


"""revision $Id: test_remove.py 215 2004-11-26 16:10:56Z Franz $
TESTS:
Assert
BuildRule
BuildTemplate
BuildDeffacts
BuildDefinstances
BuildGeneric
BuildGlobal

Fact:
  Retract

Rule:
  Remove

Template:
  Remove

Deffacts:
  Remove

Definstances:
  Remove

Generic:
  Remove

Global:
  Remove
"""

import clips
from test_00 import ctestcase

class ctc_Removals(ctestcase):
    """test builds and removals"""

    def test_RemovalsFact_01(self):
        """Testing: Assert, Fact.Retract"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            o = e.Assert('(a)')
            self.assert_(o.PPForm())
            o.Retract()
            self.assertRaises(clips.ClipsError, o.PPForm)
            self.assertRaises(clips.ClipsError, o.Retract)

    def test_RemovalsRule_01(self):
        """Testing: BuildRule, Rule.Remove"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            o = e.BuildRule('tr', '(a)', '(assert (b))')
            self.assert_(o.PPForm())
            o.Remove()
            self.assertRaises(clips.ClipsError, o.PPForm)
            self.assertRaises(clips.ClipsError, o.Remove)

    def test_RemovalsTemplate_01(self):
        """Testing: BuildTemplate, Template.Remove"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            o = e.BuildTemplate('tdt', '(slot s1)')
            self.assert_(o.PPForm())
            o.Remove()
            self.assertRaises(clips.ClipsError, o.PPForm)
            self.assertRaises(clips.ClipsError, o.Remove)

    def test_RemovalsDeffacts_01(self):
        """Testing: BuildDeffacts, Deffacts.Remove"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            o = e.BuildDeffacts('tdf', '(a)')
            self.assert_(o.PPForm())
            o.Remove()
            self.assertRaises(clips.ClipsError, o.PPForm)
            self.assertRaises(clips.ClipsError, o.Remove)

    def test_RemovalsDefinstances_01(self):
        """Testing: BuildDefinstances, Definstances.Remove"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            C = e.BuildClass("C", "(is-a USER)")
            o = e.BuildDefinstances('tdi', '(tdi1 of C)')
            self.assert_(o.PPForm())
            o.Remove()
            self.assertRaises(clips.ClipsError, o.PPForm)
            self.assertRaises(clips.ClipsError, o.Remove)

    def test_RemovalsGeneric_01(self):
        """Testing: BuildGeneric, Generic.Remove"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            o = e.BuildGeneric('g')
            self.assert_(o.PPForm())
            o.Remove()
            self.assertRaises(clips.ClipsError, o.PPForm)
            self.assertRaises(clips.ClipsError, o.Remove)

    def test_RemovalsGlobal_01(self):
        """Testing: BuildGlobal, Global.Remove"""
        for x in self.envdict.keys():
            e = self.envdict[x]
            e.Clear()
            e.Reset()
            o = e.BuildGlobal('g', clips.Integer(42))
            self.assert_(o.PPForm())
            o.Remove()
            self.assertRaises(clips.ClipsError, o.PPForm)
            self.assertRaises(clips.ClipsError, o.Remove)



# end.
