//year+pos+text.pdf

export type ProjectStatus = "obowiązujący"
| "akt indywidualny"
| "akt jednorazowy"
| "akt objęty tekstem jednolitym"
| "akt posiada tekst jednolity"
| "bez statusu"
| "brak mocy prawnej"
| "nieobowiązujący - przyczyna nieustalona"
| "nieobowiązujący - uchylona podstawa prawna"
| "obowiązujący"
| "tekst jednolity dla aktu jednorazowego"
| "uchylony"
| "uchylony wykazem"
| "uznany za uchylony"
| "wydane z naruszeniem prawa"
| "wygaśnięcie aktu"

export interface Project {
  id: number;
  address?: string;
  publisher?: string;
  year?: number;
  volume?: number;
  pos?: number;
  title?: string;
  display_address?: string;
  promulgation?: string;
  announcement_date?: Date;
  text_pdf?: boolean;
  text_html?: boolean;
  change_date?: Date
  eli?: string;
  act_type?: string;
  status?: ProjectStatus;
}

export type ConsultationStatus = 'finished' | 'ongoing' | 'planned';

export interface ProjectConsultation {
  submission_date: string;
  project_name: string;
  consultation_id: string;
  start_date: string;
  end_date: string;
  status: ConsultationStatus; // Można rozszerzyć o inne statusy
  poll_amount: number;
  project_pos: number;
}

export const PROJECT_CONSULTATIONS: ProjectConsultation[] = [
  {
    submission_date: '2025-02-21',
    project_name: 'Komisyjny projekt ustawy o zmianie ustawy - Kodeks karny wykonawczy',
    consultation_id: 'RPW/6672/2025',
    start_date: '2025-02-24',
    end_date: '2025-03-26',
    status: 'finished',
    poll_amount: 11,
    project_pos: 1110,
  },
  {
    submission_date: '2025-02-21',
    project_name: 'Poselski projekt ustawy o zmianie ustawy - Kodeks postępowania cywilnego',
    consultation_id: 'RPW/6631/2025',
    start_date: '2025-02-21',
    end_date: '2025-03-23',
    status: 'finished',
    poll_amount: 79,
    project_pos: 1143,
  },
  {
    submission_date: '2025-02-21',
    project_name: 'Poselski projekt ustawy o wystąpieniu Rzeczypospolitej Polskiej ze Światowej Organizacji Zdrowia',
    consultation_id: 'RPW/6633/2025',
    start_date: '2025-02-21',
    end_date: '2025-03-23',
    status: 'finished',
    poll_amount: 297,
    project_pos: 1114,
  },
];