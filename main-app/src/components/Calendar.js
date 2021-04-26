import '../App.css'
import {Inject,ScheduleComponent,Day,Week,Month,Agenda,WorkWeek} from '@syncfusion/ej2-react-schedule';

function Calendar() {
  return (
    <div>
        <h1>Calendar</h1>
        <ScheduleComponent currentView='Month' selectedDate={new Date(2021,0,11)}>
          <Inject services={[Day, Week, WorkWeek, Month, Agenda]}/>
        </ScheduleComponent>

    </div>
  );
}

export default Calendar;

