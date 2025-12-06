// consultation-comments.component.ts
import { CommonModule } from '@angular/common';
import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';

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
export class ConsultationCommentsComponent implements OnChanges {
  @Input() comments: ConsultationComment[] = [];

  groupedComments: CommentGroup[] = [];

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
}
