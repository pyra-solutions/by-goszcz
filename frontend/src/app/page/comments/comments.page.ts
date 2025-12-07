// // consultation-comments.component.ts
// import { CommonModule } from '@angular/common';
// import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';

// export interface ConsultationComment {
//   nr_pyt: number;
//   comment: string;
//   fullname: string;
// }


// interface CommentGroup {
//   nr_pyt: number;
//   comments: ConsultationComment[];
// }

// @Component({
//   selector: 'app-consultation-comments',
//   templateUrl: './comments.page.html',
//   styleUrls: ['./comments.page.scss'],
//   standalone: false,
// })
// export class ConsultationCommentsComponent implements OnChanges {
//   @Input() comments: ConsultationComment[] = [];

//   groupedComments: CommentGroup[] = [];

//   ngOnChanges(changes: SimpleChanges): void {
//     if (changes['comments']) {
//       this.groupComments();
//     }
//   }

//   private groupComments(): void {
//     const map = new Map<number, ConsultationComment[]>();

//     this.comments.forEach((c) => {
//       if (!map.has(c.nr_pyt)) {
//         map.set(c.nr_pyt, []);
//       }
//       map.get(c.nr_pyt)!.push(c);
//     });

//     this.groupedComments = Array.from(map.entries())
//       .sort((a, b) => a[0] - b[0])
//       .map(([nr_pyt, comments]) => ({ nr_pyt, comments }));
//   }
// }


// consultation-comments.component.ts
import { CommonModule } from '@angular/common';
import { Component, Input, OnChanges, OnInit, SimpleChanges } from '@angular/core';

export interface ConsultationComment {
  nr_pyt: number;
  comment: string;
  fullname: string;
}

interface CommentGroup {
  nr_pyt: number;
  comments: ConsultationComment[];
}

@Component({
  selector: 'app-consultation-comments',
  templateUrl: './comments.page.html',
  styleUrls: ['./comments.page.scss'],
  standalone: false,
})
export class ConsultationCommentsComponent implements OnChanges, OnInit {
  @Input() comments: ConsultationComment[] = [];

  groupedComments: CommentGroup[] = [];

  // 1. Dodałem metodę ngOnInit do inicjalizacji danych demo
  ngOnInit(): void {
    // Jeśli nie przekazano komentarzy z zewnątrz (np. z backendu), załaduj demo
    if (!this.comments || this.comments.length === 0) {
      this.comments = this.getDemoComments();
      this.groupComments(); // Ręczne wywołanie grupowania dla danych demo
    }
  }

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['comments']) {
      this.groupComments();
    }
  }

  private groupComments(): void {
    const map = new Map<number, ConsultationComment[]>();

    this.comments.forEach((c) => {
      if (!map.has(c.nr_pyt)) {
        map.set(c.nr_pyt, []);
      }
      map.get(c.nr_pyt)!.push(c);
    });

    this.groupedComments = Array.from(map.entries())
      .sort((a, b) => a[0] - b[0])
      .map(([nr_pyt, comments]) => ({ nr_pyt, comments }));
  }

  // 2. Funkcja zwracająca statyczne dane demo
  private getDemoComments(): ConsultationComment[] {
    return [
      {
        nr_pyt: 1,
        fullname: 'Jan Kowalski',
        comment: 'Uważam, że proponowane zmiany w planie zagospodarowania są krokiem w dobrą stronę, ale brakuje mi szczegółów dotyczących terenów zielonych.'
      },
      {
        nr_pyt: 1,
        fullname: 'Anna Nowak',
        comment: 'Zgadzam się z przedmówcą. Zieleń miejska powinna być priorytetem.'
      },
      {
        nr_pyt: 2,
        fullname: 'Piotr Wiśniewski',
        comment: 'Czy budżet na rok 2025 uwzględnia remont ulicy Długiej? W dokumencie nie widzę takiej pozycji.'
      },
      {
        nr_pyt: 3,
        fullname: 'Maria Zielińska',
        comment: 'Brak uwag do tego punktu. Wszystko wydaje się jasne.'
      },
      {
        nr_pyt: 3,
        fullname: 'Tomasz Lewandowski',
        comment: 'Proponuję wydłużenie terminu konsultacji o kolejne 7 dni, dokumenty są bardzo obszerne.'
      },
      {
        nr_pyt: 4,
        fullname: 'Krzysztof Krawczyk',
        comment: 'To pytanie jest źle sformułowane, sugeruje odpowiedź. Proszę o korektę.'
      }
    ];
  }
}