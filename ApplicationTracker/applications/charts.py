import pygal

from .models import Application

class RecruitmentFunnel():

    def __init__(self, **kwargs):
        self.chart = pygal.Funnel(**kwargs)
        self.chart.title = 'Recruitment Funnel'

    def get_data(self, user=None):
        data = {
        'Application_Submitted': 0,
        'Phone_Screen': 0,
        'Technical_Interview': 0,
        'On_Site_Interview': 0,
        'Job_Offer': 0,
        }

        if user != None:
            for application in Application.objects.filter(user=user):
                if application.status:
                    status = application.status.replace(' ', '_')
                    data[status] += 1
        else:
            applications = Application.objects.all()
            for application in applications:
                if application.status:
                    status = application.status.replace(' ', '_')
                    data[status] += 1
            
            for label in data:
                count = data[label]
                data[label] = count / len(applications) * 100

        return data

    def generate(self, user=None):
        chart_data = self.get_data(user)

        for key, value in chart_data.items():
            self.chart.add(key, value)

        return self.chart.render(is_unicode=True)