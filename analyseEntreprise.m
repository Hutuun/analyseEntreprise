clear();
%%clf();

X = load("bilan_X.txt");
Y = matlab.io.datastore.DsFileReader("bilan_secteurs.txt");

if hasdata(Y)
    [d,count] = read(Y,100000,'SizeMethod','OutputSize',...
                                       'OutputType','char');
end



si = size(X);

n = si(1);

Von = zeros(si(1),1);

for i = 1:si(1)
    for j = 1:si(2)
       if X(i,j) == -1.0
           Von(i) = -1.0;
           n = n-1;
           break;
       end
    end
end

res = zeros(n,si(2));
ta = 0;

for i = 1:si(1)
    if Von(i) == 0
        ta = ta+1;
        res(ta,:) = X(i,:);
    end
end