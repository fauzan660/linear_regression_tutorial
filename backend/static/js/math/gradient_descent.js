export default class GradientDescent {
    constructor(X, y){
        this.X = X;
        this.y = y;
    }
    gradient(w, b) {
        // 'm' represents the total number of features (area sizes)
        var x = this.X;
        var y = this.y;
        const m = x.length;
        
        // Initialize the partial derivatives of the cost function
        let dj_dw = 0;
        let dj_db = 0;
    
        // Calculate the sum of partial derivatives for each feature
        for (let i = 0; i < m; i++) {
            const f_wb = w * x[i] + b;
            const dj_dw_i = (f_wb - y[i]) * x[i];
            const dj_db_i = f_wb - y[i];
            dj_dw += dj_dw_i;
            dj_db += dj_db_i;
        }
    
        // Calculate the average of the partial derivatives
        dj_dw / m;
        dj_db / m;
        
        return [dj_dw, dj_db];
    }
    cost(w, b) {
        var x = this.X;
        var y = this.y;

        // 'm' represents the total number of features (area sizes)
        const m = x.length;
        
        // 'f_wb' is the linear regression prediction value given 'x', 'w', and 'b'
        var f_wb = 0;
        
        // Initialize cost as 0
        var cost = 0;
    
        // Calculate the sum of squared differences between predicted and actual values
        for (let i = 0; i < m; i++) {
            f_wb = w * x[i] + b;
            cost += Math.pow(f_wb - y[i], 2);
        }
    
        // Calculate the mean squared error (cost function value)
        const j_wb = cost;
    
        return j_wb;
    }
}