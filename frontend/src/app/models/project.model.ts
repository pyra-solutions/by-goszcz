//year+pos+text.pdf

export type ProjectStatus =  "akt indywidualny"
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