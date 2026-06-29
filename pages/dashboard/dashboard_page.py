from playwright.sync_api import Page, expect

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)
        self.navbar = NavbarComponent(page)
        self.students_chart = ChartViewComponent(page, identifier='students', chart_type='bar')
        self.activities_chart = ChartViewComponent(page, identifier='activities', chart_type='line')
        self.courses_chart = ChartViewComponent(page, identifier='courses', chart_type='pie')
        self.scores_chart = ChartViewComponent(page, identifier='scores', chart_type='scatter')
        self.dashboard_toolbar_view = DashboardToolbarViewComponent(page)


    def check_visible_dashboard_title(self):
        self.dashboard_toolbar_view.check_visible()

    def check_visible_students_chart(self):
        self.students_chart.check_visible(title='Students')

    def check_visible_courses_chart(self):
        self.courses_chart.check_visible(title='Courses')

    def check_visible_activities_chart(self):
        self.activities_chart.check_visible(title='Activities')

    def check_visible_scores_chart(self):
        self.scores_chart.check_visible(title='Scores')