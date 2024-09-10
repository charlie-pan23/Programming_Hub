function optimal_sol_value = findNextTheta(theta, d)
    % 定义k的具体值
    k = 0.55 / (2 * pi);
    
    % 引入符号计算功能
    syms x

    % 定义c1和c2
    c1 = k*theta*cos(theta);
    c2 = k*theta*sin(theta);

    % 定义方程
    eq = k^2*x^2 - 2*k*c1*x*cos(x) - 2*k*c2*x*sin(x) + c1^2 + c2^2 == d^2;

    % 使用vpasolve进行数值求解，指定搜索区间
    sol_num = vpasolve(eq, x, [theta,32*pi]);  % 注意：这里将搜索区间改为从0到32*pi，以确保覆盖足够的范围%%

    % 定义一个小的容忍度epsilon
    epsilon = 1e-4;  % 例如，使用1e-6作为容忍度

    % 检查是否找到解
    if isempty(sol_num)
        optimal_sol_value = -1000; % 如果没有找到符合条件的解
    else
        % 将解转换为双精度数组，方便处理
        sols = double(sol_num);

        % 筛选出大于theta的解，引入容忍度epsilon
        valid_sols = sols(sols > theta + epsilon);%%

        % 如果没有符合条件的解
        if isempty(valid_sols)
            optimal_sol_value = -1000; % 如果没有找到大于theta的解
        else
            % 找到x - theta值最小的解
            [~, idx] = min(valid_sols - theta);
            optimal_sol_value = valid_sols(idx); % 返回符合条件的解的数值
        end
    end
end
