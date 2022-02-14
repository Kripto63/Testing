#!/usr/bin/perl

# У нас есть массив:
# my @unsorted = ( qw/ 7 1 3 4 2 4 6 5 5 / );
# Напиши алгоритм, который отсортирует этот массив. Пользоваться встроенной функцией sort нельзя. Для простоты можно написать алгоритм bubble sort.
# Напиши алгоритм двоичного поиска. Если поиск элемента удачный, должно выводиться MATCH, если неудачный - NOT_MATCH.

my @unsorted=(qw/ 7 1 3 4 2 4 6 5 5 /);
my $count = scalar(@unsorted);
my $temp;

print "@unsorted \n";

for (my $i=0; $i<$count - 1; $i++){
    for (my $j=0; $j<$count-i; $j++) {
        if ($unsorted[$j] > $unsorted[$j + 1]) {
            $temp = $unsorted[$j];
            $unsorted[$j] = $unsorted[$j + 1];
            $unsorted[$j+1] = $temp;
        }  
    }    
}

print "@unsorted\n";

my $key = 8;
my $start = 0;
my $end = scalar(@unsorted);
my $midpoint = 0;

while($start <= $end){

    $midpoint = int(int($start + $end) / 2);

    if($key == @unsorted[$midpoint]){
        print "MATCH";
        $start = $end + 1;
    } elsif(int($end - $start) / 2 == 0) {
        print "NOT_MATCH";
        $start = $end + 1;
    } elsif($key < @unsorted[$midpoint]) {
        $end = $midpoint - 1
    } elsif($key > @unsorted[$midpoint]) {
        $start = $midpoint + 1
    }
}