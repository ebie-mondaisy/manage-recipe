from application import app, db
from flask import url_for
from flask_testing import TestCase
from application.models import *
from datetime import date

class TestBase(TestCase):

    def create_app(self):
        #setting up app config
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            SECRET_KEY='secretkeytest',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        #create elements needed before each test
        db.create_all()
        testa = Cuisines(cuisName="Dutch")
        testb = makeRecipe(recipeName="pancakes", creatorName="sandy", description="things", ingredients="apple", instructions="happy", calories="43", difficulty="easy", CuisID=1)
        testc = trackCook(madeDate=date(2010, 3, 3), success="satisfactory", enjoyRate=7, notes="details", recipe_id=1)
        db.session.add(testa)
        db.session.add(testb)
        db.session.add(testc)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

#testing the home/index route
class TestHomeView(TestBase):
    def test_getHome(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)

#testing the routes that allow the creation of recipes, cuisines and notes
class TestCreate(TestBase):
    def test_addRecipe(self):
        response = self.client.post(url_for('create'), 
        data=dict(recipeName="testrecipe", 
                    creatorName="testcreator", 
                    description="testdesc", 
                    ingredients="testing", 
                    instructions="testinst", 
                    calories=43, 
                    difficulty="advanced",
                    cuisName=1), 
                    follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"", response.data)

class TestCreateCuisine(TestBase):
    def test_addCuisine(self):
        response = self.client.post(url_for('create_cuisine'), data=dict(cuisName="TestCuisine"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"TestCuisine", response.data)

class TestUpdate(TestBase):
    def test_update(self):
        response1 = self.client.post(url_for('edit_recipe', id = 1), 
        data=dict(recipeName="waffles", 
        creatorName="beached", 
        description="cook", 
        ingredients="egg", 
        instructions="smile", 
        calories=54, 
        difficulty="easy"), 
        follow_redirects=True)
        response = self.client.post(url_for('edit_recipe', id=1), 
            data=dict(madeDate='2003-03-04', 
            success="satisfactory", 
            enjoyRate=8, 
            notes="notes"), 
            follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"", response.data)
        response2 = self.client.get(url_for('edit_recipe', id = 1))
        self.assertEqual(response1.status_code, 200)
        self.assert200(response2)
        self.assertIn(b"", response1.data)

#testing the cuisine view page on the application
class TestCuisineView(TestBase):
    def test_getCuisine(self):
        response = self.client.get(url_for('cuisine_view'))
        self.assert200(response)

#testing the deletion of recipes and notes from the database
class TestDeleteRecipe(TestBase):
    def test_deleteRecipe(self):
        response = self.client.post(url_for('delete', id=1), follow_redirects=True)
        assert response.status_code == 200

class TestDeleteNote(TestBase):
    def test_deleteNote(self):
        response = self.client.post(url_for('delete_track', id=1), data=dict(track_ID=1))
        assert response.status_code == 200

#testing the search functionality of the application
class TestSearchRecipe(TestBase):
    def test_searchRecipe(self):
        response = self.client.post(url_for('search_recipe'), data=dict(recipe_name="cupcakes"), follow_redirects=True)
        self.assert200(response)
        self.assertIn(b"", response.data)