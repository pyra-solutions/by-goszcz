export type ProjectStatus = 'W TOKU' | 'ZAKOŃCZONY' | 'OCZEKUJE';

export interface Project {
  id: number;
  title: string;
  description: string;
  status: ProjectStatus;
  updatedAt: Date;
}
